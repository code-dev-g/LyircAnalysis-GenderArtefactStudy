class Tokenizer():

    '''
    Tokenizer class for tokenizing the text data
    
    Split Modes:

        1. 'space' - split the text on space
    
        2. 'periods' - split the text on periods and spaces
    
        3. 'nonalphanumeric' - split the text on non-alphanumeric characters

        4. 'newline' - split the text on newline characters
        
        5. 'custom' - split the text on custom characters

    '''

    def __init__(self, split_mode, custom_chars=None):
        self.split_modes = split_mode
        self.custom_chars = custom_chars

    def tokenize(self, text):
        '''
        Convert to the required character set and tokenize the text based on the split mode
        '''

        if self.split_modes == 'space':
            return self.tokenize_space(text)
        elif self.split_modes == 'periods':
            return self.tokenize_periods(text)
        elif self.split_modes == 'specialchars':
            return self.tokenize_specialchars(text)
        elif self.split_modes == 'newline':
            return self.tokenize_newline(text)
        elif self.split_modes == 'custom':
            return self.tokenize_custom(text)
        else:
            raise ValueError('Invalid split mode')
        
    def tokenize_space(self, text):
        '''
        Split the text on space
        '''
        return text.split()
    
    def tokenize_periods(self, text):
        '''
        Split the text on periods and spaces
        '''
        import re
        return re.split('[. ]', text)
    
    def tokenize_specialchars(self, text):
        '''
        Split the text on non-alphanumeric characters
        '''
        
        import re
        words = re.split(r'[`\-=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>? ]', text)
        words = [word for word in words if word != '']
        return words

    
    def tokenize_newline(self, text):
        '''
        Split the text on newline characters
        '''
        return text.split('\n')
    
    def tokenize_custom(self, text):
        '''
        Split the text on custom characters
        '''
        import re
        words = re.split('[{}]'.format(self.custom_chars), text)
        words = [word for word in words if word != '']
        return words