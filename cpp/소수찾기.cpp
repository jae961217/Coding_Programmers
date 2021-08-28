#include<string>
#include<vector>
#include<algorithm>
#include<set>

using namespace std;

bool isPrime(int n)
{
	if (n < 2) return false;

	for (int i = 2; i <= sqrt(n); i++)
		if (n % i == 0) return false;

	return true;
}

int solution(string numbers)
{
	int answer = 0;
	vector<char> v;
	vector<int> nums;

	for (int i = 0; i < numbers.size(); i++)
	{
		v.push_back(numbers[i]);
	}
	sort(v.begin(), v.end());

	do
	{
		string tmp = "";
		for (int i = 0; i < v.size(); i++)
		{
			tmp.push_back(v[i]);
			nums.push_back(stoi(tmp));
		}
	} while (next_permutation(v.begin(), v.end()));

	sort(nums.begin(), nums.end());
	nums.erase(unique(nums.begin(), nums.end()), nums.end());

	for (int i = 0; i < nums.size(); i++)
	{
		if (isPrime(nums[i]))
			answer++;
	}

	return answer;
}