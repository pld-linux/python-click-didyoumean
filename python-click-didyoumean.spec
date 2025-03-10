#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Enable git-like "did-you-mean" feature in click
Summary(pl.UTF-8):	Włączenie funkcji "czy miałeś na myśli" w stylu gita w clicku
Name:		python-click-didyoumean
# keep 0.0.x here for python2 support
Version:	0.0.3
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/click-didyoumean/
Source0:	https://files.pythonhosted.org/packages/source/c/click-didyoumean/click-didyoumean-%{version}.tar.gz
# Source0-md5:	08ac34aa0355f58ffc43ee57f1969ffb
URL:		https://pypi.org/project/click-didyoumean/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-click
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-click
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enable git-like "did-you-mean" feature in click.

%description -l pl.UTF-8
Włączenie funkcji "czy miałeś na myśli" w stylu gita w clicku.

%package -n python3-click-didyoumean
Summary:	Enable git-like "did-you-mean" feature in click
Summary(pl.UTF-8):	Włączenie funkcji "czy miałeś na myśli" w stylu gita w clicku
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-click-didyoumean
Enable git-like "did-you-mean" feature in click.

%description -n python3-click-didyoumean -l pl.UTF-8
Włączenie funkcji "czy miałeś na myśli" w stylu gita w clicku.

%prep
%setup -q -n click-didyoumean-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/click_didyoumean
%{py_sitescriptdir}/click_didyoumean-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-click-didyoumean
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/click_didyoumean
%{py3_sitescriptdir}/click_didyoumean-%{version}-py*.egg-info
%endif
