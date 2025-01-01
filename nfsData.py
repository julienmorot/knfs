## Contains the nfs data structure
## Originaly written by Red Hat for system-config-nfs
## Copyright (C) 2002 Red Hat, Inc.
## Copyright (C) 2002 Brent Fox <bfox@redhat.com>

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from qt import *

class nfsData(QListViewItem):

    def __init__(self, listview):
        QListViewItem.__init__(self, listview)
        self.directory = None
        self.hosts = None
        self.permissions = "ro"
        self.insecure = None
        self.sync = "sync"
        self.no_wdelay = None
        self.no_subtree_check = None
        self.insecure_locks = None
        self.no_root_squash = None
        self.all_squash = None
        self.anonuid = None
        self.anongid = None

    def set_directory(self, data):
        self.directory = data
    
    def set_hosts(self, data):
        self.hosts = data
    
    def set_permissions(self, data):
        self.permissions = data
    
    def set_insecure(self, data):
        self.insecure = data
    
    def set_sync(self, data):
        self.sync = data
    
    def set_no_wdelay(self, data):
        self.no_wdelay = data
    
    def set_no_subtree_check(self, data):
        self.no_subtree_check = data
    
    def set_insecure_locks(self, data):
        self.insecure_locks = data
    
    def set_no_root_squash(self, data):
        self.no_root_squash = data
    
    def set_all_squash(self, data):
        self.all_squash = data
    
    def set_anonuid(self, data):
        self.anonuid = data
    
    def set_anongid(self, data):
        self.anongid = data
    
    def get_directory(self):
        return self.directory
    
    def get_hosts(self):
        return self.hosts
    
    def get_permissions(self):
        return self.permissions
    
    def get_insecure(self):
        return self.insecure
    
    def get_sync(self):
        return self.sync
    
    def get_no_wdelay(self):
        return self.no_wdelay
    
    def get_no_subtree_check(self):
        return self.no_subtree_check
    
    def get_insecure_locks(self):
        return self.insecure_locks
    
    def get_no_root_squash(self):
        return self.no_root_squash
    
    def get_all_squash(self):
        return self.all_squash
    
    def get_anonuid(self):
        return self.anonuid
    
    def get_anongid(self):
        return self.anongid
    
    def set_col_directory(self):
        self.setText(0, self.get_directory())

    def set_col_hosts(self):
        self.setText(1, self.get_hosts())

    def set_col_perms(self):
        if self.permissions == "ro":
            self.setText(2, "Read Only")
        else:
            self.setText(2, "Read/Write")
