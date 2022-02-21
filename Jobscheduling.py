# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1#
class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        job_count = 0
        profit = 0
        Jobs.sort(reverse=True, key = lambda x: x.profit)
        max_deadline = 0
        for job in Jobs:
            if job.deadline > max_deadline:
                max_deadline = job.deadline
        track = [False] * max_deadline
        for job in Jobs:
            d = job.deadline
            i = d - 1
            for i in range(d-1, -1, -1):
                if track[i] == False:
                    profit += job.profit
                    job_count += 1
                    track[i] = True
                    break

        return (job_count, profit)