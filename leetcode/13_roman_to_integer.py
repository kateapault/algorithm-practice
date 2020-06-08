def romanToInt(self, s: str) -> int:
        roman = {
            'I':{
                'position': 7,
                'value': 1
            },
            'V':{
                'position':6,
                'value':5
            },
            'X':{
                'position':5,
                'value':10
            },
            'L':{
                'position':4,
                'value':50
            },
            'C':{
                'position':3,
                'value':100
            },
            'D':{
                'position':2,
                'value':500
            },
            'M':{
                'position':1,
                'value':1000
            }
        }
        
        total = 0
        i = 0
        
        while i < len(s):
            if i < len(s)-1 and roman[s[i]]['position'] > roman[s[i+1]]['position']:
                total += (roman[s[i+1]]['value'] - roman[s[i]]['value'])
                i += 2
            else:
                total += roman[s[i]]['value']
                i += 1
        
        return total