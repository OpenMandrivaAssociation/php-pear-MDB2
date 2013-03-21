%define		_class		MDB2
%define		upstream_name	%{_class}
%define		beta b5

Name:		php-pear-%{upstream_name}
Version:	2.5.0
Release:	0.0.%{beta}
Summary:	Unified database API
Epoch:		2
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/MDB2/
Source0:	http://download.pear.php.net/package/MDB2-%{version}%{beta}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
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
%setup -q -c -n %{name}-%{version}%{beta}
mv package.xml %{upstream_name}-%{version}%{beta}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}%{beta}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data/%{upstream_name}/LICENSE

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%doc %{upstream_name}-%{version}%{beta}/docs/*
%doc %{upstream_name}-%{version}%{beta}/LICENSE
%{_datadir}/pear/%{_class}
%{_datadir}/pear/%{_class}.php
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2:2.5.0-0.0.b3.1mdv2011.0
+ Revision: 679275
- 1.5.0b3

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2:2.5.0-0.0.b2.3
+ Revision: 667564
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2:2.5.0-0.0.b2.2mdv2011.0
+ Revision: 607115
- rebuild

* Fri Mar 26 2010 Oden Eriksson <oeriksson@mandriva.com> 2:2.5.0-0.0.b2.1mdv2010.1
+ Revision: 527640
- 2.5.0b2
- fix versioning

* Thu Nov 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1:2.5.0b1-7mdv2010.1
+ Revision: 470286
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1:2.5.0b1-6mdv2010.0
+ Revision: 426652
- rebuild

* Wed Dec 31 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.5.0b1-5mdv2009.1
+ Revision: 321872
- rebuild

* Fri Oct 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.5.0b1-4mdv2009.1
+ Revision: 294597
- added php-pear-MDB2_Driver_mysql as a suggest as well

* Sat Sep 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.5.0b1-3mdv2009.0
+ Revision: 281929
- suggest some drivers

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1:2.5.0b1-2mdv2009.0
+ Revision: 224753
- rebuild

* Tue Mar 25 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.5.0b1-1mdv2008.1
+ Revision: 189940
- 2.5.0b1 (fixes CVE-2007-5934)

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.1-2mdv2008.1
+ Revision: 178523
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri May 04 2007 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.1-1mdv2008.0
+ Revision: 22353
- 2.4.1

* Thu Apr 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.0-1mdv2008.0
+ Revision: 15130
- 2.4.0


* Fri Dec 15 2006 David Walluck <walluck@mandriva.org> 2.3.0-1mdv2007.0
+ Revision: 97219
- 2.3.0

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1:2.2.1-2mdv2007.1
+ Revision: 81174
- Import php-pear-MDB2

* Wed Aug 30 2006 David Walluck <walluck@mandriva.org> 1:2.2.1-2mdv2007.0
- add missing Native directory

* Wed Aug 30 2006 David Walluck <walluck@mandriva.org> 1:2.2.1-1mdv2007.0
- 2.2.1
- replace tabs with spaces

* Fri May 26 2006 David Walluck <walluck@mandriva.org> 1:2.0.3-1mdv2007.0
- 2.0.3

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1:2.0.2-1mdk
- 2.0.2
- rule out some faulty deps

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdk
- initial Mandriva package (PLD import)


