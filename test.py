class Rule:
    ...
    
    
class MyRule(Rule):
    def __init__(self, value=0):
        self.check_value = value
        
    def check(self):
        return self.checked_value
    
    @property
    def checked_value(self):
        
        @property
        def value(self):
            return self.check_value
        
        return value


rule = MyRule(value=114514)
