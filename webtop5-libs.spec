Summary: WebTop5 libs
Name: webtop5-libs
Version: 1.1.4
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
# Source1 can be downloaded executing: webtop5-build.sh
Source1: webtop-webapp-5.war
Source2: http://www.sonicle.com/nethesis/webtop5/postgresql-8.0-312.jdbc3.jar
BuildArch: noarch
Conflicts: webtop4-libs

# Do not repack JARs to avoid file date
# Should be safe: https://www.redhat.com/archives/fedora-devel-java-list/2008-September/msg00042.html
%define __jar_repack %{nil}

BuildRequires: unzip

%description
NethServer WebTop 5 libraries

%prep
%setup

%build
mkdir -p root/var/lib/tomcats/webtop/webapps/webtop
mkdir -p root/usr/share/java/tomcat
mv %{SOURCE2} root/usr/share/java/tomcat
unzip %{SOURCE1} \
 *jar \
 -x *sonicle*.jar \
 -x *webtop*.jar \
 -d root/var/lib/tomcats/webtop/webapps/webtop

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})

%post

%preun

%files
%defattr(-,root,root)
/var/lib/tomcats/webtop/webapps/webtop/*
/usr/share/java/tomcat/postgresql-8.0-312.jdbc3.jar

%changelog
* Mon Sep 04 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.4-1
- Release WebTop 5.0.13 - NethServer/dev#5338

* Thu Jun 22 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.3-1
- Replace upstream managesive library - NethServer/dev#5312

* Tue Jun 13 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.2-1
- Release WebTop 5.0.9 - NethServer/dev#5312

* Fri Jun 09 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.1-1
- Release WebTop 5.0.7 (tag 5.0.8) - NethServer/dev#5312

* Wed May 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- WebTop 5: enable folder sorting - NethServer/dev#5275
- Build RPM from source

* Wed Mar 08 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- First WebTop5 release - NethServer/dev#5225

