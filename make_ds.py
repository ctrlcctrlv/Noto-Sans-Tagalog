import os

from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, RuleDescriptor, InstanceDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "NotoSansTagalog"

#------
# axes
#------

axis = AxisDescriptor()
axis.maximum = 700
axis.minimum = 400
axis.default = 400
axis.name = "weight"
axis.tag = "wght"
doc.addAxis(axis)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = "NotoSansTagalog-Regular.ufo"
s0.name = "master.NotoSansTagalog.Regular.0"
s0.familyName = familyName
s0.styleName = "Regular"
s0.location = dict(weight=400)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = "NotoSansTagalog-Bold.ufo"
s1.name = "master.NotoSansTagalog.Bold.0"
s1.familyName = familyName
s1.styleName = "Bold"
s1.location = dict(weight=700)
doc.addSource(s1)

#-----------
# instances
#-----------

i0 = InstanceDescriptor()
i0.name = 'instance_Regular'
i0.familyName = familyName
i0.styleName = "Regular"
i0.path = os.path.join(root, "instances", "NotoSansTagalog-Regular.ufo")
i0.location = dict(weight=400)
i0.kerning = True
i0.info = True
doc.addInstance(i0)

i1 = InstanceDescriptor()
i1.name = 'instance_Medium'
i1.familyName = familyName
i1.styleName = "Medium"
i1.path = os.path.join(root, "instances", "NotoSansTagalog-Medium.ufo")
i1.location = dict(weight=500)
i1.kerning = True
i1.info = True
doc.addInstance(i1)

i2 = InstanceDescriptor()
i2.name = 'instance_SemiBold'
i2.familyName = familyName
i2.styleName = "SemiBold"
i2.path = os.path.join(root, "instances", "NotoSansTagalog-SemiBold.ufo")
i2.location = dict(weight=600)
i2.kerning = True
i2.info = True
doc.addInstance(i2)

i3 = InstanceDescriptor()
i3.name = 'instance_Bold'
i3.familyName = familyName
i3.styleName = "Bold"
i3.path = os.path.join(root, "instances", "NotoSansTagalog-Bold.ufo")
i3.location = dict(weight=700)
i3.kerning = True
i3.info = True
doc.addInstance(i3)

#-------
# rules
#-------

r1 = RuleDescriptor()
r1.name = "ra_crossing"
r1.conditionSets.append([dict(name="weight", minimum=(300*.75)+400, maximum=700)])
r1.subs.append(("uni170D", "uni170D.avar"))
doc.addRule(r1)

r2 = RuleDescriptor()
r2.name = "ya_gap"
r2.conditionSets.append([dict(name="weight", minimum=(300*.75)+400, maximum=700)])
r2.subs.append(("uni170C", "uni170C.avar"))
doc.addRule(r2)

#--------
# saving
#--------

path = os.path.join(root, "NotoSansTagalog.designspace")
doc.write(path)
