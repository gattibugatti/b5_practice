class Timing:
	def __init__(self,function_to_run):
		self.num_runs = 100
		self.func_to_run = function_to_run

	def __call__(self,*args,**kwargs):
		avg = 0
		for _ in range(self.num_runs):
			t0 = time.time()
			self.func_to_run(*args, **kwargs)
			t1 = time.time()
			avg += (t1 - t0)
		avg /= self.num_runs
		fn = self.func_to_run.__name__
		print(
			"[Timing] Avg время выполнеия %s за %s запусков: %.5f сек" %
			(fn, self.num_runs, avg)
			)
		return self.func_to_run(*args, **kwargs)
    def __enter__(self):
    	self.t0 = time.time()
    	return
    def __exit__(self, *args):
    	t1 = time.time()
    	avg_time = (t1 - self.t0)
    	print('Разница - {}'.format(avg_time))
