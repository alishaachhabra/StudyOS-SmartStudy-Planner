#include "trie.h"
#include <cctype>

using namespace std;

Trie::Trie()
{
    root = new TrieNode();
}

void Trie::insert(string word)
{
    TrieNode* current = root;

    for(char ch : word)
    {
        ch = tolower(ch);

        if(ch<'a' || ch>'z')
            continue;

        int index = ch-'a';

        if(current->children[index]==nullptr)
            current->children[index]=new TrieNode();

        current=current->children[index];
    }

    current->isEnd=true;
}

bool Trie::search(string word)
{
    TrieNode* current=root;

    for(char ch:word)
    {
        ch=tolower(ch);

        if(ch<'a'||ch>'z')
            continue;

        int index=ch-'a';

        if(current->children[index]==nullptr)
            return false;

        current=current->children[index];
    }

    return current->isEnd;
}

void Trie::collectWords(
    TrieNode* node,
    string current,
    vector<string>& result
)
{
    if(node==nullptr)
        return;

    if(node->isEnd)
        result.push_back(current);

    for(int i=0;i<26;i++)
    {
        if(node->children[i]!=nullptr)
        {
            collectWords(
                node->children[i],
                current+char(i+'a'),
                result
            );
        }
    }
}

vector<string> Trie::startsWith(string prefix)
{
    TrieNode* current=root;

    for(char ch:prefix)
    {
        ch=tolower(ch);

        if(ch<'a'||ch>'z')
            continue;

        int index=ch-'a';

        if(current->children[index]==nullptr)
            return {};

        current=current->children[index];
    }

    vector<string> result;

    collectWords(current,prefix,result);

    return result;
}