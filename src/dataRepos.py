class DataRepos():

    __slots__ = [
        '_name',
        '_full_name',
        '_description',
        '_language',
        '_created_at',
        '_updated_at'
    ]

    def __init__(self, 
        name = '',
        full_name = '', 
        description = '',
        language = '',
        created_at = '',
        updated_at = '' ):
        self._name = self.name = name
        self._full_name = self.full_name = full_name
        self._description = self.description = description
        self._language = self.language = language
        self._created_at = self.created_at = created_at
        self._updated_at = self.updated_at = updated_at
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name=''):
        self._name = name
    
    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, full_name=''):
        self._full_name = full_name
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description=''):
        self._description = description
    
    @property
    def language(self):
        return self._language
    
    @language.setter
    def language(self, language=''):
        self._language = language
    
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at=''):
        self._created_at = created_at
    
    @property
    def updated_at(self):
        return self._updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at=''):
        self._updated_at = updated_at
    
    


    def print_repo(self):
        print(self.name)
        print(self.full_name)
        print(self.description)
        print(self.language)
        print(self.created_at)
        print(self.updated_at)