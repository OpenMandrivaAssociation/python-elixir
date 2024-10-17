%define module_name Elixir

Summary:	Declarative mapper on top of SQLAlchemy
Name:		python-elixir
Version:	0.7.1
Release:	2
License:	MIT
Group:		Development/Python
URL:		https://www.sqlalchemy.org/
Source0:	http://pypi.python.org/packages/source/E/%{module_name}/%{module_name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:   python-sqlalchemy

%description
A declarative layer on top of SQLAlchemy. It is a fairly thin wrapper, which 
provides the ability to create simple Python classes that map directly to 
relational database tables (this pattern is often referred to as the Active 
Record design pattern), providing many of the benefits of traditional databases
without losing the convenience of Python objects.

Elixir is intended to replace the ActiveMapper SQLAlchemy extension, and the 
TurboEntity project but does not intend to replace SQLAlchemy's core features, 
and instead focuses on providing a simpler syntax for defining model objects 
when you do not need the full expressiveness of SQLAlchemy's manual mapper 
definitions.

%prep
%setup -q -n %{module_name}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}

%__python setup.py install --skip-build --root=%{buildroot} --install-purelib=%{python_sitelib}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README 
%{python_sitelib}/elixir
%{python_sitelib}/%{module_name}-%{version}-py*.egg-info/


%changelog
* Thu Jan 28 2010 Frederik Himpe <fhimpe@mandriva.org> 0.7.1-1mdv2010.1
+ Revision: 497766
- Update to new version 0.7.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6.1-3mdv2010.0
+ Revision: 442102
- rebuild

* Mon Mar 16 2009 Michael Scherer <misc@mandriva.org> 0.6.1-2mdv2009.1
+ Revision: 355571
- add missing Requires on SQLAlchemy

* Mon Mar 16 2009 Michael Scherer <misc@mandriva.org> 0.6.1-1mdv2009.1
+ Revision: 355563
- import python-elixir


