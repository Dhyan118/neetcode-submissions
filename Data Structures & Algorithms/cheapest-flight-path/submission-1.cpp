class Solution 
{
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        vector<pair<int, int>> adj[n];

        for (auto H : flights){
            adj[H[0]].push_back({H[1], H[2]});
        } 

        queue<pair<int,pair<int, int>>> q;
        q.push({0, {src, 0}});

        vector<int> dist(n, 1e9);
        dist[src] = 0;

        while(!q.empty()){
            auto H = q.front();
            q.pop();

            int stops = H.first;
            int node = H.second.first;
            int cost = H.second.second;

            if (stops > k) continue;

            for( auto H1 : adj[node]){
                int adjNode = H1.first;
                int edw = H1.second;
                
                if(cost + edw < dist[adjNode] && stops <= k){
                    dist[adjNode] = cost + edw;
                    q.push({stops + 1, {adjNode, cost+edw}});
                }
            }
        }

        if(dist[dst] == 1e9) return -1;
        return dist[dst];
    }
};
