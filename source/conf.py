breathe_default_project = "test"

breathe_projects = {
    "test":"../xml",
    }

extensions = [ "breathe" ]

root_doc = 'contents'
master_doc = 'contents'

breathe_default_members = ('members', 'undoc-members')

cpp_id_attributes = [ 'threadsafe', 'static', 'const', 'variable/c', 'variable' ]
cpp_paren_attributes = [ ]
