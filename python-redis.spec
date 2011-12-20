%define		module	redis
Summary:	A Python client for redis
Name:		python-%{module}
Version:	2.4.9
Release:	1
License:	MIT
Group:		Development/Languages
URL:		http://github.com/andymccurdy/redis-py
Source0:	http://github.com/downloads/andymccurdy/redis-py/%{module}-%{version}.tar.gz
# Source0-md5:	b512ff37d06c6813f04a57f6448a1e55
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python interface to the Redis key-value store.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-*.egg-info
