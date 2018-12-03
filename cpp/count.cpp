#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <pthread.h>
using namespace std;

/**
 * In the assi we need to read and write to a file therefore we user the iostream and fstream 
 * and since we will be counting occurences map is the best solution (it will sort the values by keys by default)
 */
void writeResultToFiles(map<string, int> words)
{
    // open files
    ofstream result;
    result.open("result.txt");
    // write map to file
    for (map<string, int>::iterator wit = words.begin(); wit != words.end(); ++wit)
        result << wit->first << ":\t" << wit->second << endl;
    // close file
    result.close();
}

int main(int argc, char *argv[])
{

    ifstream file;
    file.open(argv[2]);
    if (!file.is_open())
        return 1;
    map<string, int> words;
    while (file.good())
    {
        string s;
        getline(file, s);
        int pos = s.find_first_of(' ');
        if (pos < 0)
            continue;
        while (s.size() > 0)
        {
            pos = s.find_first_of(' ');
            if (pos < 0)
                pos = s.size();
            string word = s.substr(0, pos);
            if (word != "")
                words[word]++;
            s = s.erase(0, pos + 1);
        }
    }

    // write result
    writeResultToFiles(words);

    return 0;
}