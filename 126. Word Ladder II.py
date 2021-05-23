def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # bfs with memory
        wordDict = set(wordList)
        if endWord not in wordDict: return []
        l, s, used, flag, parent = len(beginWord), {beginWord}, set(), True, defaultdict(list)
        while s and flag:
            tmp = set()
            used = used.union(s)
            for w in s:
                new_word = [w[:i] + x + w[i+1:] for x in string.ascii_lowercase for i in range(l)]
                for x in new_word:
                    if x == endWord: flag = False
                    if x in wordDict and x not in used:
                        tmp.add(x)
                        parent[w].append(x)
            if not tmp: return []
            s = tmp
        # dfs    
        ans = []
        def dfs(cur, pos):
            if pos == endWord: 
                ans.append(cur.copy())
                return
            for p in parent[pos]:
                cur.append(p)
                dfs(cur, p)
                cur.pop()
        dfs([beginWord], beginWord)
        return ans
