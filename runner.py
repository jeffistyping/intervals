from interval import Interval

class Runner:

  def run(self):
    interval = Interval([(1,4),(3,5),(7,9)])
    print(f'Initial Dataset: {interval}')
    interval.Delete((2,3))
    print(f'Delete(2,3): {interval}')
    interval.Add((10,14))
    print(f'Add(10,14): {interval}')
    interval.Delete((1,8))
    print(f'Delete(1,8): {interval}')
    print("Get(8,16): ",interval.Get((8,16)))
    
if __name__ == "__main__":
  try:
    Runner().run()
  except KeyboardInterrupt:
    print("~~~~~~~~~Program Stopped")