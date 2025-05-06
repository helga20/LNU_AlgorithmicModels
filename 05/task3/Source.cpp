#include <iostream>
#include <vector>
#include <windows.h> 

using namespace std;

//������� ����� ���������� �����
void printCheckpoint(const string& message, const vector<int>& data) {
    cout << "���������� ����� - " << message << " [";
    for (size_t i = 0; i < data.size(); i++) {
        cout << data[i] << (i < data.size() - 1 ? ", " : "");
    }
    cout << "]" << endl;
}

vector<int> longestIncreasingSubsequence(const vector<int>& sequence) {
    vector<int> longest, current;

    for (size_t i = 0; i < sequence.size(); i++) {
        //���������� ����� - ������� ��������� �����
        cout << "���������� �����- ������������ ����� " << sequence[i] << endl;

        if (i == 0 || sequence[i] > sequence[i - 1]) {
            current.push_back(sequence[i]);
        }
        else {
            if (current.size() > longest.size()) {
                longest = current;
            }
            current = { sequence[i] };
        }

        //���������� ����� - ������� ��������� �������������
        printCheckpoint("������� ��������� �������������", current);
    }

    if (current.size() > longest.size()) {
        longest = current;
    }

    return longest;
}

int main() {

    SetConsoleCP(1251);         
    SetConsoleOutputCP(1251);

    vector<int> numbers;
    int n;
    cout << "������ ������� ��������: ";
    cin >> n;
    numbers.resize(n);

    cout << "������ �����: ";
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    printCheckpoint("������� �����������", numbers);

    vector<int> result = longestIncreasingSubsequence(numbers);

    printCheckpoint("�������� ��������� �������������", result);

    return 0;
}
