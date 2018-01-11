import collections
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ex_time = collections.defaultdict(int)
        stack = []
        for i in xrange(len(logs)):
            print ex_time
            log_list = logs[i].split(":")
            #print log_list
            fun_id = int(log_list[0])
            start_end = log_list[1]
            time_stamp = int(log_list[2])
            if i==0:
                stack.append((fun_id, start_end,time_stamp))
                continue
            if not stack:stack.append((fun_id, start_end,time_stamp))
            elif start_end=="end"  and fun_id == stack[-1][0] and stack[-1][1] =="start":
                #print "funnnnnnid", fun_id
                tem_id, tem_start_end,tem_time_sta = stack.pop()
                tem_exe_time = time_stamp-tem_time_sta+1
                
                ex_time[fun_id]+=tem_exe_time
                if not stack:
                    continue
                else:
                    print "stack his", stack
                    for his_id, his_sta_end, his_time in stack:
                        if his_id == fun_id:
                         #   stack.pop()
                            ex_time[fun_id]-=tem_exe_time
                            break
                        ex_time[his_id]-=tem_exe_time
            else:stack.append((fun_id,start_end, time_stamp))
        #print "#####", stack 
        res = []
        for i in range(n):  
            res.append(ex_time[i])
        return res

n=1
logs = ["0:start:0","0:start:1","0:start:2","0:end:3","0:end:4","0:end:5"]
a=Solution()
print a.exclusiveTime( n, logs)
