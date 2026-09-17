#ifndef TRIE_H
#define TRIE_H

#include <string>
#include <vector>

using namespace std;

class TrieNode
{
public:

    bool isEnd;

    TrieNode* children[26];

    TrieNode()
    {
        isEnd = false;

        for(int i=0;i<26;i++)
            children[i]=nullptr;
    }
};

class Trie
{
private:

    TrieNode* root;

    void collectWords(
        TrieNode* node,
        string current,
        vector<string>& result
    );

public:

    Trie();

    void insert(string word);

    bool search(string word);

    vector<string> startsWith(string prefix);
};

#endif