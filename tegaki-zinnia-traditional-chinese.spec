Summary: Traditional Chinese Models for tegaki zinnia engine
Name: tegaki-zinnia-traditional-chinese
Version: 0.3
Release: %mkrel 1
License: GPLv2+
Group: System/Internationalization
Source0: http://www.tegaki.org/releases/0.3/models/%{name}-%{version}.zip
URL: http://www.tegaki.org
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
BuildArch: noarch
Requires: locales-zh_TW
Requires: tegaki
Requires: zinnia
Provides: tegaki-models

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%prep
%setup -qn %name-%version

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/tegaki/models/zinnia/
install -m0644 *.meta *.model %{buildroot}%{_datadir}/tegaki/models/zinnia/

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%{_datadir}/tegaki/models/zinnia/*
