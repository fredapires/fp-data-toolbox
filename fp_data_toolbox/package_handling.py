# =============================================
# General Package Handling


# DONE function for pip installing from a provided github https url
def pip_install_from_github_url(github_url):
    import os
    print('Running "pip install" command using '+github_url)
    os.system('pip install git+'+github_url)


def pipenv_install_from_github_url(github_url):
    import os
    print('Running "pip install" command using '+github_url)
    os.system('pipenv install git+'+github_url)
