%define		_class		MDB2
%define		upstream_name	%{_class}

%define		_requires_exceptions pear(test_setup.php)\\|pear(MDB2/Schema.php)\\|pear(PHPUnit.php)

Name:		php-pear-%{upstream_name}
Version:	2.5.0
Release:	%mkrel 0.0.b2.1
Summary:	Unified database API
Epoch:		2
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/MDB2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}b2.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
Suggests:	php-pear-MDB2_Driver_mysql
Suggests:	php-pear-MDB2_Driver_mysqli
Suggests:	php-pear-MDB2_Driver_pgsql
Suggests:	php-pear-MDB2_Driver_sqlite
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
MDB2 is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

%prep
%setup -q -c -n %{name}-%{version}b2
mv package.xml %{upstream_name}-%{version}b2/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}b2
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/%{upstream_name}/LICENSE

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}b2/docs/*
%doc %{upstream_name}-%{version}b2/LICENSE
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml
