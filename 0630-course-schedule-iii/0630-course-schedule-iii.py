class Solution:
	def scheduleCourse(self, courses: List[List[int]]) -> int:
		if len(courses)==0:
			return 0

		courses.sort(key=lambda x:x[1])
		duration, time =[], 0

		for course in courses:
			if course[0]+time<=course[1]:
				heappush(duration,-course[0])
				time += course[0]
			else:
				if duration:
					if course[0] <- duration[0]:
						time -= -(heappop(duration))
						time += course[0]
						heappush(duration,-course[0])
                        
		return len(duration)