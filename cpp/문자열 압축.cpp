#include <string>
#include <vector>

using namespace std;

vector<pair<string, int>> v;

int num(int n)
{
	int count = 0;
	if (n < 10)
		return 1;
	while (n >= 10)
	{
		n /= 10;
		count++;
	}
	return count + 1;
}

int solution(string s) {
	int answer = s.length();
	int count = 0;


	for (int i = 1; i <= s.length() / 2; i++)
	{
		v.clear();
		count = 0;
		for (int j = 0; j < s.length() - i + 1; j = j + i)
		{
			bool check = false;
			string tmp = s.substr(j, i);
			if (count == 0)
			{
				v.push_back({ tmp,1 });
				count++;
				continue;
			}

			if (v[count - 1].first == tmp)
			{
				v[count - 1].second++;
				check = true;
			}
			if (!check)
			{
				v.push_back({ tmp,1 });
				count++;
			}

		}
		int value = 0;
		if (s.length() % i != 0)
		{
			value += s.length() % i;
		}


		for (int j = 0; j < count; j++)
		{
			value += v[j].first.length();
			if (v[j].second != 1)
				value += num(v[j].second);

		}
		if (answer > value)
			answer = value;
	}

	return answer;
}