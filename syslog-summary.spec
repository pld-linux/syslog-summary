Summary:	Summarize the contents of a syslog log file
Name:		syslog-summary
Version:	1.14
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	https://github.com/downloads/dpaleino/syslog-summary/%{name}-%{version}.tar.gz
# Source0-md5:	c1f0bed6664bc429d2679405dcb8fc11
URL:		https://launchpad.net/syslog-summary
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program summarizes the contents of a log file written by syslog,
by displaying each unique (except for the time) line once, and also
the number of times such a line occurs in the input. The lines are
displayed in the order they occur in the input.

It is also possible to define some "ignore rules" using regular
expressions.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/%{name},%{_bindir},%{_mandir}/man1}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -p %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/ignore.rules
%attr(755,root,root) %{_bindir}/syslog-summary
%{_mandir}/man1/syslog-summary.1*
