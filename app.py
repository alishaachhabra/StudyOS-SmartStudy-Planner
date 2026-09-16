from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
import uuid
from database.models import db, User, Subject, Task
from datetime import datetime
from datetime import date
import random

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY", "studyos-dev-secret")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studyos.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- COLORS ---------------- #

COLORS = [
    "#6366F1",
    "#3B82F6",
    "#22C55E",
    "#F97316",
    "#EC4899",
    "#14B8A6",
    "#FACC15"
]

ICONS = [
    "📘",
    "📗",
    "📙",
    "📕",
    "📒",
    "📓",
    "📔"
]


# ---------------- MOTIVATIONAL QUOTES ---------------- #

quotes = [

    "Small progress every day leads to big results.",

    "Don't compare yourself with others. Compare yourself with yesterday.",

    "Success is built through consistency.",

    "Your dreams are valid, your efforts matter.",

    "Every challenge makes you stronger.",

    "Stay consistent. Progress follows.",

    "Discipline beats motivation.",

    "Success is earned every single day."

]


# ---------------- SPLASH ---------------- #

@app.route("/")
def splash():
    return render_template("splash.html")


# ---------------- WELCOME ---------------- #

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")


# ---------------- LOGIN ---------------- #

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        user = User.query.filter_by(
            email=email
        ).first()

        if user:

            if user.password == password:

                session["user_id"] = user.id
                session["user_name"] = user.name

                return redirect(url_for("dashboard"))

            return "Incorrect Password"

        return "Account doesn't exist. Please Sign Up."

    return render_template("login.html")


# ---------------- SIGNUP ---------------- #

@app.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        dob = request.form["dob"]

        password = request.form["password"]

        confirm_password = request.form["confirm_password"]

        if password != confirm_password:

            return "Passwords do not match"

        existing_user = User.query.filter_by(
            email=email
        ).first()

        if existing_user:

            return "Email already registered."

        user = User(

    name=name,

    email=email,

    dob=dob,

    password=password,

    profile_pic="default.png"

)

        db.session.add(user)

        db.session.commit()

        return redirect(url_for("login"))

    return render_template("signup.html")
# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("login"))

    hour = datetime.now().hour

    if hour < 12:
        greeting = "Good Morning ☀️"
    elif hour < 17:
        greeting = "Good Afternoon 🌤️"
    else:
        greeting = "Good Evening 🌙"

    subjects = Subject.query.filter_by(
        user_id=session["user_id"]
    ).all()

    tasks = Task.query.filter_by(
        user_id=session["user_id"]
    ).all()

    total_subjects = len(subjects)

    pending_tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Pending"
    ).count()

    completed_tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Completed"
    ).count()

    high_priority = Task.query.filter_by(
        user_id=session["user_id"],
        importance=3,
        status="Pending"
    ).count()

    today = date.today()

    due_today = 0

    for task in tasks:

        if task.deadline == today and task.status == "Pending":
            due_today += 1

    if pending_tasks + completed_tasks == 0:
        progress = 0
    else:
        progress = int(
            (completed_tasks / (pending_tasks + completed_tasks)) * 100
        )

    return render_template(

        "dashboard.html",

        greeting=greeting,

        quote=random.choice(quotes),

        user_name=session["user_name"],

        subjects=subjects,

        total_subjects=total_subjects,

        pending_tasks=pending_tasks,

        high_priority=high_priority,

        due_today=due_today,

        progress=progress

    )


# ---------------- SUBJECTS ---------------- #

@app.route("/subjects")
def subjects():

    if "user_id" not in session:
        return redirect(url_for("login"))

    subjects = Subject.query.filter_by(
        user_id=session["user_id"]
    ).all()

    return render_template(

        "subjects.html",

        subjects=subjects,

        user_name=session["user_name"]

    )


@app.route("/add_subject", methods=["POST"])
def add_subject():

    if "user_id" not in session:
        return redirect(url_for("login"))

    subject_name = request.form["subject_name"].strip()

    existing = Subject.query.filter_by(

        user_id=session["user_id"],

        subject_name=subject_name

    ).first()

    if existing:

        return redirect(url_for("subjects"))

    total = Subject.query.filter_by(
        user_id=session["user_id"]
    ).count()

    color = COLORS[total % len(COLORS)]

    icon = ICONS[total % len(ICONS)]

    subject = Subject(

        user_id=session["user_id"],

        subject_name=subject_name,

        color=color,

        icon=icon

    )

    db.session.add(subject)

    db.session.commit()

    return redirect(url_for("subjects"))


@app.route("/delete_subject/<int:id>")
def delete_subject(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    subject = Subject.query.get_or_404(id)

    Task.query.filter_by(subject_id=id).delete()

    db.session.delete(subject)

    db.session.commit()

    return redirect(url_for("subjects"))
# ---------------- TASKS ---------------- #

@app.route("/tasks")
def tasks():

    if "user_id" not in session:
        return redirect(url_for("login"))

    subjects = Subject.query.filter_by(
        user_id=session["user_id"]
    ).all()

    tasks = Task.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Task.deadline.asc()).all()

    return render_template(
        "tasks.html",
        user_name=session["user_name"],
        subjects=subjects,
        tasks=tasks
    )


@app.route("/add_task", methods=["POST"])
def add_task():

    if "user_id" not in session:
        return redirect(url_for("login"))

    deadline = datetime.strptime(
        request.form["deadline"],
        "%Y-%m-%d"
    ).date()

    task = Task(

        user_id=session["user_id"],

        subject_id=int(request.form["subject_id"]),

        task_name=request.form["task_name"],

        deadline=deadline,

        estimated_time=int(request.form["estimated_time"]),

        importance=int(request.form["importance"]),

        mandatory=("mandatory" in request.form),

        status="Pending",

        notes=request.form["notes"]

    )

    db.session.add(task)

    db.session.commit()

    return redirect(url_for("tasks"))


@app.route("/complete_task/<int:id>")
def complete_task(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    task.status = "Completed"

    db.session.commit()

    return redirect(url_for("tasks"))

# ----------------AIplanner ---------------- #
@app.route("/delete_task/<int:id>")
def delete_task(id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    task = Task.query.get_or_404(id)

    db.session.delete(task)

    db.session.commit()

    return redirect(url_for("tasks"))

@app.route("/aiplanner")
def aiplanner():

    if "user_id" not in session:
        return redirect(url_for("login"))

    return render_template(
        "aiplanner.html",
        user_name=session["user_name"]
    )

@app.route("/generate_plan", methods=["POST"])
def generate_plan():

    if "user_id" not in session:
        return redirect(url_for("login"))

    available_time = int(request.form["study_time"])

    tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Pending"
    ).all()

    if len(tasks) == 0:

        return render_template(
            "plan.html",
            user_name=session["user_name"],
            plan=[],
            available_time=available_time,
            total_time=0
        )

    # -------- Priority Score -------- #

    for task in tasks:

        score = 0

        if task.importance == 3:
            score += 50

        elif task.importance == 2:
            score += 30

        else:
            score += 10

        if task.mandatory:
            score += 30

        today = date.today()

        days_left = (task.deadline - today).days

        if days_left <= 0:
            score += 40

        elif days_left == 1:
            score += 30

        elif days_left <= 3:
            score += 20

        else:
            score += 10

        task.priority_score = score

    tasks.sort(
        key=lambda x: x.priority_score,
        reverse=True
    )

    plan = []

    used_time = 0

    for task in tasks:

        if used_time + task.estimated_time <= available_time:

            plan.append(task)

            used_time += task.estimated_time

    return render_template(

        "plan.html",

        user_name=session["user_name"],

        plan=plan,

        available_time=available_time,

        total_time=used_time

    )
# ---------------- CALENDAR ---------------- #

@app.route("/calendar")
def calendar():

    if "user_id" not in session:
        return redirect(url_for("login"))

    tasks = Task.query.filter_by(
        user_id=session["user_id"]
    ).order_by(Task.deadline.asc()).all()

    return render_template(
        "calendar.html",
        user_name=session["user_name"],
        tasks=tasks
    )


# ---------------- ANALYTICS ---------------- #

@app.route("/analytics")
def analytics():

    if "user_id" not in session:
        return redirect(url_for("login"))

    total_subjects = Subject.query.filter_by(
        user_id=session["user_id"]
    ).count()

    total_tasks = Task.query.filter_by(
        user_id=session["user_id"]
    ).count()

    completed_tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Completed"
    ).count()

    pending_tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Pending"
    ).count()

    high_priority = Task.query.filter_by(
        user_id=session["user_id"],
        importance=3,
        status="Pending"
    ).count()

    if total_tasks == 0:
        completion = 0
    else:
        completion = int((completed_tasks / total_tasks) * 100)

    return render_template(

        "analytics.html",

        user_name=session["user_name"],

        total_subjects=total_subjects,

        total_tasks=total_tasks,

        completed_tasks=completed_tasks,

        pending_tasks=pending_tasks,

        high_priority=high_priority,

        completion=completion

    )

# ---------------- STUDY COACH ---------------- #

@app.route("/studycoach")
def studycoach():

    if "user_id" not in session:
        return redirect(url_for("login"))

    pending = Task.query.filter_by(
        user_id=session["user_id"],
        status="Pending"
    ).count()

    if pending == 0:
        message = "🎉 Great job! You have completed all your tasks."
    else:
        message = f"You have {pending} pending task(s). Let's finish them!"

    return render_template(
        "studycoach.html",
        user_name=session["user_name"],
        message=message
    )


# ---------------- PROFILE ---------------- #

@app.route("/upload_profile", methods=["POST"])
def upload_profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    if "profile_pic" not in request.files:
        return redirect(url_for("profile"))

    file = request.files["profile_pic"]

    if file.filename == "":
        return redirect(url_for("profile"))

    filename = secure_filename(file.filename)

    extension = os.path.splitext(filename)[1]

    new_filename = str(uuid.uuid4()) + extension

    upload_folder = os.path.join(
        app.root_path,
        "static",
        "profile"
    )

    os.makedirs(upload_folder, exist_ok=True)

    file.save(
        os.path.join(upload_folder, new_filename)
    )

    user = User.query.get(session["user_id"])

    user.profile_pic = new_filename

    db.session.commit()

    return redirect(url_for("profile"))

@app.route("/profile")
def profile():

    if "user_id" not in session:
        return redirect(url_for("login"))

    user = User.query.get(session["user_id"])

    total_subjects = Subject.query.filter_by(
        user_id=session["user_id"]
    ).count()

    total_tasks = Task.query.filter_by(
        user_id=session["user_id"]
    ).count()

    completed_tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Completed"
    ).count()

    pending_tasks = Task.query.filter_by(
        user_id=session["user_id"],
        status="Pending"
    ).count()

    return render_template(

        "profile.html",

        user=user,

        total_subjects=total_subjects,

        total_tasks=total_tasks,

        completed_tasks=completed_tasks,

        pending_tasks=pending_tasks

    )

# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
