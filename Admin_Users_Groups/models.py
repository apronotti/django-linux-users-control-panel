# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.db import models
from .osprocess import osprocess
import sys

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=50, default='', blank=True, null=True)
    passwordrt = models.CharField(max_length=50, default='', blank=True, null=True)
    osproc = osprocess()
    labels = {
        'password': _('Password'),
        'passwordrt' : _('Repeat password'),
    }

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def delete(self, *args, **kwargs):
        self.osproc.deleteUser(self.name)
        if (self.osproc.execResult):
            super(User, self).delete(*args, **kwargs)
        else:
            print >> sys.stdout, "output: %s " % (self.osproc.output)
            print >> sys.stdout, "erroroutput: %s " % (self.osproc.erroroutput)
        return self.osproc.erroroutput
        
    def save(self, *args, **kwargs):
        if (self.pk is None):
            self.name = self.name.lower()
            self.osproc.agregaUsuario(self.name, self.password)
        else:
            pass
            # modify
            
        if (self.osproc.execResult):
            self.password = "ClaveAsignada"
            self.passwordrt = "ClaveAsignada"
            super(User, self).save(*args, **kwargs)
        else:
            print >> sys.stdout, "output: %s " % (self.osproc.output)
            print >> sys.stdout, "erroroutput: %s " % (self.osproc.erroroutput)
        
        return self.osproc.erroroutput
        
            


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(User,blank=True)
    osproc = osprocess()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

    def delete(self, *args, **kwargs):
        self.osproc.deleteGroup(self.name)
        if (self.osproc.execResult):
            super(Group, self).delete(*args, **kwargs)
        else:
            print >> sys.stdout, "output: %s " % (self.osproc.output)
            print >> sys.stdout, "erroroutput: %s " % (self.osproc.erroroutput)
        return self.osproc.erroroutput

    def save(self, *args, **kwargs):
        if (self.pk is None):
            self.name = self.name.lower()
            self.osproc.addGroup(self.name)
            # add
            #self.name = self.name + "+"
        else:
            pass
            # modify

        if (self.osproc.execResult):            
             super(Group, self).save(*args, **kwargs)
        else:
            print >> sys.stdout, "output: %s " % (self.osproc.output)
            print >> sys.stdout, "erroroutput: %s " % (self.osproc.erroroutput)
        
        return self.osproc.erroroutput

