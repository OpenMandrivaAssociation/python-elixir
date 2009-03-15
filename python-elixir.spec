%define module_name Elixir

Summary:	Declarative mapper on top of SQLAlchemy
Name:		python-elixir
Version:	0.6.1
Release:	%mkrel 1
License:	MIT
Group:		Development/Python
URL:		http://www.sqlalchemy.org/
Source0:	http://pypi.python.org/packages/source/E/%{module_name}/%{module_name}-%{version}.tar.gz
BuildRequires:	python-devel
BuildRequires:	python-setuptools
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
%doc CHANGES LICENSE README  examples
%{python_sitelib}/elixir
%{python_sitelib}/%{module_name}-%{version}-py*.egg-info/
