###################################################################################
#	Marvell GPL License
#	
#	If you received this File from Marvell, you may opt to use, redistribute and/or
#	modify this File in accordance with the terms and conditions of the General
#	Public License Version 2, June 1991 (the "GPL License"), a copy of which is
#	available along with the File in the license.txt file or by writing to the Free
#	Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 or
#	on the worldwide web at http://www.gnu.org/licenses/gpl.txt.
#	
#	THE FILE IS DISTRIBUTED AS-IS, WITHOUT WARRANTY OF ANY KIND, AND THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE ARE EXPRESSLY
#	DISCLAIMED.  The GPL License provides additional details about this warranty
#	disclaimer.
###################################################################################

from distutils.sysconfig import get_python_lib
import os
import imp
import sys


def import_external(main_module, parent='Marvell'):
    module_name = "{}.{}".format(parent, main_module)
    if not sys.modules.get(module_name, False):
        external_sources = os.path.join(get_python_lib(), parent)
        external_sources = os.path.join(external_sources, main_module)

        f, filename, description = imp.find_module(main_module, [os.path.dirname(external_sources)])
        imp.load_module(module_name, f, filename, description)




