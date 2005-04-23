"""
$Id: __init__.py,v 1.16 2005/04/23 00:16:54 jccooper Exp $
"""

from AccessControl.Permissions import add_user_folders
from Products.CMFCore.DirectoryView import registerDirectory
from Products.PluggableAuthService import registerMultiPlugin
from Products.CMFPlone import PloneUtilities as plone_utils

import config

#################################
# plugins
from plugins import gruf
from plugins import user
from plugins import group
from plugins import role
from plugins import local_role
from plugins import ufactory

#################################
# pas monkies
import pas                              

#################################
# pas monkies 2 play w/ gruf
if config.PAS_INSIDE_GRUF:
    import gruf_support

#################################
# plone monkies
import plone

#################################
# new groups tool
from tools.groups import GroupsTool

registerDirectory('skins', globals())

#################################
# register plugins with pas
try:
    registerMultiPlugin( gruf.GRUFBridge.meta_type )
    registerMultiPlugin( user.UserManager.meta_type )
    registerMultiPlugin( group.GroupManager.meta_type )    
    registerMultiPlugin( role.GroupAwareRoleManager.meta_type )
    registerMultiPlugin( local_role.LocalRolesManager.meta_type )
    registerMultiPlugin( ufactory.PloneUserFactory.meta_type )
except RuntimeError:
    # make refresh users happy
    pass

def initialize(context):

    tools = ( GroupsTool, )

    plone_utils.ToolInit('PlonePAS Tools',
                         tools=tools,
                         product_name='PlonePAS',
                         icon='tool.gif',
                         ).initialize(context)
                         
    
    context.registerClass( role.GroupAwareRoleManager,
                           permission = add_user_folders,
                           constructors = ( role.manage_addGroupAwareRoleManagerForm,
                                            role.manage_addGroupAwareRoleManager ),
                           visibility = None
                           )
    
    context.registerClass( gruf.GRUFBridge,
                           permission = add_user_folders,
                           constructors = ( gruf.manage_addGRUFBridgeForm,
                                            gruf.manage_addGRUFBridge ),
                           visibility = None
                           )

    context.registerClass( user.UserManager,
                           permission = add_user_folders,
                           constructors = ( user.manage_addUserManagerForm,
                                            user.manage_addUserManager ),
                           visibility = None
                           )

    context.registerClass( group.GroupManager,
                           permission = add_user_folders,
                           constructors = ( group.manage_addGroupManagerForm,
                                            group.manage_addGroupManager ),
                           visibility = None
                           )                           

    context.registerClass( ufactory.PloneUserFactory,
                           permission = add_user_folders,
                           constructors = ( ufactory.manage_addPloneUserFactoryForm,
                                            ufactory.manage_addPloneUserFactory ),
                           visibility = None
                           )                           

    context.registerClass( local_role.LocalRolesManager,
                           permission = add_user_folders,
                           constructors = ( local_role.manage_addLocalRolesManagerForm,
                                            local_role.manage_addLocalRolesManager ),
                           visibility = None
                           )                           
