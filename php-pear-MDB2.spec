%define _class		MDB2
%define modname	%{_class}
%define beta b5

Summary:	Unified database API
Name:		php-pear-%{modname}
Epoch:		2
Version:	2.5.0
Release:	0.0.%{beta}
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/MDB2/
Source0:	http://download.pear.php.net/package/MDB2-%{version}%{beta}.tgz
BuildArch:	noarch
BuildRequires:	php-pear
Requires(post,preun):	php-pear
Requires:	php-pear
Suggests:	php-pear-MDB2_Driver_mysql
Suggests:	php-pear-MDB2_Driver_mysqli
Suggests:	php-pear-MDB2_Driver_pgsql
Suggests:	php-pear-MDB2_Driver_sqlite

%description
MDB2 is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

%prep
%setup -qc -n %{name}-%{version}%{beta}
mv package.xml %{modname}-%{version}%{beta}/%{modname}.xml

%install
cd %{modname}-%{version}%{beta}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/%{modname}/LICENSE

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%doc %{modname}-%{version}%{beta}/docs/*
%doc %{modname}-%{version}%{beta}/LICENSE
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{modname}.xml

