def func(queue):
        res = []
        while queue:
            level_len = count = len(queue)
            level_sum = 0
            while count:
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
                count -= 1
            res.append(level_sum / level_len)
        return res