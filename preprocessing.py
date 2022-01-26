class Normalize(object):
    def __init__(self):
        pass
    
    def __call__(self, x):
        return self.normalize(x)
    
    def normalize(self, values):
        return (values - min(values))/max(values)


class Smooth(object):
    def __init__(self, weight):
        self.weight = weight
    
    def __call__(self, x):
        return self.smooth(x)
    
    def smooth(self, values):
        """exponential moving average"""
        last = values[0]

        smoothed_values = []
        for value in values:
            smoothed_values.append(self.weight * value + (1 - self.weight) * last)
            last = smoothed_values[-1]

        return smoothed_values


class Transform(object):
    def __init__(self, transforms):
        self.transforms = transforms
    
    def __call__(self, x):
        for transform in self.transforms:
            x = transform(x)
        return x
