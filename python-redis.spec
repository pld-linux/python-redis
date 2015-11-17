#
# Conditional build:
%bcond_with	tests	# perform tests (seem to require redis running)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	redis
Summary:	A Python client for redis
Name:		python-%{module}
Version:	2.10.5
Release:	1
License:	MIT
Group:		Development/Languages
URL:		http://github.com/andymccurdy/redis-py
Source0:	https://pypi.python.org/packages/source/r/redis/redis-2.10.5.tar.gz
# Source0-md5:	3b26c2b9703b4b56b30a1ad508e31083
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
%if %{with python2}
BuildRequires:	python-setuptools
%{?with_tests:BuildRequires:	python-pytest}
%endif
%if %{with python3}
BuildRequires:	python3-setuptools
%{?with_tests:BuildRequires:	python3-pytest}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python interface to the Redis key-value store.

%package -n python3-%{module}
Summary:	A Python client for redis
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This is a Python interface to the Redis key-value store.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%{__python} setup.py build --build-base build-2 %{?with_tests:test}
%endif

%if %{with python3}
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGES README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-*.egg-info
