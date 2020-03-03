
import math

class create_ts:

      def __init__(self,signal_type="Harmonic",weight=0.001,noise_type="white",trend_type="Linear",length_of_ts=1000,num_of_points=500):
        
        self.signal_type=signal_type
        self.weight=weight
        self.noise_type=noise_type
        self.trend_type=trend_type
        self.length_of_ts=length_of_ts
        self.num_points=num_of_points
        self.time_sampler = ts.TimeSampler(stop_time=self.length_of_ts)
        self.irregular_time_samples = self.time_sampler.sample_regular_time(num_points=self.num_points)


      def sample_data(self,gaussian_kernel="Periodic",frequency_ratio=0.1,num_points=500,trend_type="linear"):
          if self.signal_type=="Harmonic":
                self.signal = ts.signals.Sinusoidal(frequency_ratio)
          else:
                self.signal = ts.signals.GaussianProcess(kernel='Periodic', nu=3./2)    

          if noise=="white":
                  self.noise = ts.noise.GaussianNoise(std=0.25)
          else:
                  self.noise = ts.noise.RedNoise(std=0.5, tau=0.8)    

          timeseries = ts.TimeSeries(self.signal, noise_generator=self.noise) 


          samples, signals, errors = timeseries.sample(self.irregular_time_samples)    

          if trend_type=='linear':
             samples=add_linear_trend(samples)
          elif trend_type=='exp':
             samples=add_exp_trend(samples)
          elif trend_type=='log':
             samples=add_log_trend(samples)
          else :
             samples=add_polynomial_trend(samples)         

          return samples,self.irregular_time_samples


      def add_linear_trend(x):
          new_trend=[]
          for i,point in enumerate(x) :
            point=1+self.weight*i+point
            new_trend.append(point)
          return new_trend  

      def add_exp_trend(x):
          new_trend=[]
          for i,point in enumerate(x) :
            point=math.exp(self.weight*i)+point
            new_trend.append(point)
          return new_trend 

      def add_log_trend(x):
          new_trend=[]
          for i,point in enumerate(x) :
            point=math.log(i+1)+point
            new_trend.append(point)
          return new_trend

      def add_polynomial_trend(x):
          new_trend=[]
          for i,point in enumerate(x):
            point=(pow(i+1,2)*self.weight)+point
            new_trend.append(point)
          return new_trend      
                    



