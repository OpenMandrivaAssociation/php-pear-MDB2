%define         _class          MDB2
%define         _pearname       %{_class}
%define         _status         stable

%define         _requires_exceptions pear(test_setup.php)\\|pear(MDB2/Schema.php)\\|pear(PHPUnit.php)

Summary:        %{_pearname} - unified database API
Name:           php-pear-%{_pearname}
Version:        2.4.1
Release:        %mkrel 2
Epoch:          1
License:        PHP License
Group:          Development/PHP
URL:            http://pear.php.net/package/MDB2/
Source0:        http://pear.php.net/get/%{_pearname}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:       php-pear
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot

%description
MDB2 is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs %{__perl} -pi -e 's|\r$||g'

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/Driver/{Datatype,Function,Manager,Native,Reverse}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/
install %{_pearname}-%{version}/%{_class}/*.php %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/%{_class}/Driver/Datatype/*.php %{buildroot}%{_datadir}/pear/%{_class}/Driver/Datatype/
install %{_pearname}-%{version}/%{_class}/Driver/Function/*.php %{buildroot}%{_datadir}/pear/%{_class}/Driver/Function/
install %{_pearname}-%{version}/%{_class}/Driver/Manager/*.php %{buildroot}%{_datadir}/pear/%{_class}/Driver/Manager/
install %{_pearname}-%{version}/%{_class}/Driver/Native/*.php %{buildroot}%{_datadir}/pear/%{_class}/Driver/Native/
install %{_pearname}-%{version}/%{_class}/Driver/Reverse/*.php %{buildroot}%{_datadir}/pear/%{_class}/Driver/Reverse/

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
        if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
                %{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
        fi
fi
if [ "$1" = "2" ]; then
        if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
                %{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
        fi
fi

%preun
if [ "$1" = 0 ]; then
        if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
                %{_bindir}/pear uninstall --nodeps -r %{_pearname}
        fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs/,tests/}
%{_datadir}/pear/*.php
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{_pearname}.xml


