# this will give the available package versions
# pip install package==

def packages_1():
  if pip.__version__ >= "10.0.0":
      from pip._internal.utils.misc import get_installed_distributions
  else:
      from pip import get_installed_distributions
  sorted(["%s==%s" % (i.key, i.version) for i in get_installed_distributions()])

def packages_2():
  from pkg_resources import working_set
  sorted(["%s==%s" % (d.project_name, d.version) for d in working_set])
