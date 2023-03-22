class Employee:
    def __init__(self, name, ID, DOJ, salary, bonus=0.0):
        self.name  = name
        self.ID = ID
        self.DOJ = DOJ
        self.salary = salary
        self.bonus = bonus
        
    def get_bonus(self):
        return self.bonus
    
    def set_bonus(self, bonus):
        self.bonus = bonus
        
    # name, ID, DOJ, salary, bonus
        
    def __str__(self):
        
        string = self.name        + ',' + \
                 self.ID          + ',' + \
                 self.DOJ         + ',' + \
                 str(self.salary) + ',' + \
                 str(self.bonus)
                          
        return string
        
        