import os
from fp_data_toolbox import package_handling

input_url='https://github.com/fredapires/fp_data_toolbox'
package_handling.pip_install_from_github_url(input_url)

input_url='https://github.com/fredapires/mtg-proj'
package_handling.pip_install_from_github_url(input_url)
