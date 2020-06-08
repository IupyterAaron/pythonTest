def allPassed(self):
    if self.mathScore<60 or self.engScore<60 or self.proScore<60:
        return False
    else:
        return True