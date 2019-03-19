# pip install package==

def packages():
  if pip.__version__ >= "10.0.0":
      from pip._internal.utils.misc import get_installed_distributions
      sorted(["%s==%s" % (i.key, i.version) for i in get_installed_distributions()])
  else:
      from pip import get_installed_distributions
      sorted(["%s==%s" % (i.key, i.version) for i in get_installed_distributions()])
