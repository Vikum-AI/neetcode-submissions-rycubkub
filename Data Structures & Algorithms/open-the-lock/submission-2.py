class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)

        if '0000' in deadends:
            return -1
        
        res = 0
        seen = set()
        queue = deque(['0000'])

        while queue:
            size = len(queue)
            print(queue)

            for s in range(size):
                node = queue.popleft()

                if node == target:
                    return res

                for i in range(4):
                    if int(node[i]) < 9:
                        nei1 = node[:i] + str(int(node[i])+1) + node[i+1:]

                        if nei1 not in deadset and nei1 not in seen:
                            seen.add(nei1)
                            queue.append(nei1)
                    else:
                        nei1 = node[:i] + '0' + node[i+1:]

                        if nei1 not in deadset and nei1 not in seen:
                            seen.add(nei1)
                            queue.append(nei1)
                    
                    if int(node[i]) > 0:
                        nei2 = node[:i] + str(int(node[i])-1) + node[i+1:]

                        if nei2 not in deadset and nei2 not in seen:
                            seen.add(nei2)
                            queue.append(nei2)
                    else:
                        nei1 = node[:i] + '9' + node[i+1:]

                        if nei1 not in deadset and nei1 not in seen:
                            seen.add(nei1)
                            queue.append(nei1)

            res += 1      

        return -1