#include<iostream>
#include<cmath>
#include<vector>
#include<algorithm>
#include<iomanip>
#include<utility>
#include<queue>

using namespace std;

//bfs для того щоб просто вивести порядок проходу алгоритму по вершинах

vector<int> bfs(vector<vector<int>> adj, int start){
    
    vector<int> res;

    int n = adj.size();

    queue<int> q;
    
    vector<bool> visited(n, false);

    visited[start] = true;

    q.push(start);

    while(!q.empty()){
        int current = q.front();
        q.pop();
        res.push_back(current);

        for(int x: adj[current]){
            if(!visited[x]){
                visited[x] = true;
                q.push(x);
            }
        }
    }
    return res;
}

int main(){

    cout << "BFS" << endl;

    int n, m;
    cout << "Enter  and m: ";
    cin >> n >> m;

    vector<vector<int>> adj(n + 1);
    for(int i = 0; i < m; i++){
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }


   return 0;
}