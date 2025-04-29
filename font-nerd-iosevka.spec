%global urlbase https://github.com/ryanoasis/nerd-fonts/releases/download/v%{version}
%global debug_package %{nil}

Name:		font-nerd-iosevka
Version:	3.4.0
Release:	1
Source0:	%{urlbase}/iosevka.tar.xz
Summary:	Iconic font aggregator, collection, and patcher
URL:		https://github.com/ryanoasis/nerd-fonts
License:	MIT and OFL-1.1
Group:		System/Fonts/True type
BuildArch:      noarch

%package -n fonts-ttf-iosevka
Group:		System/Fonts/Open type
Summary:	Iconic font set

%description -n fonts-otf-awesome
Iconic font set

%description
%summary
%prep
%autosetup -c

%install
install -d %{buildroot}%{_datadir}/fonts/TFF %{buildroot}%{_docdir}/%{name} %{buildroot}%{_licensedir}/%{name}
install -m644 *.ttf %{buildroot}%{_datadir}/fonts/TFF
install -m644 README.md %{buildroot}%{_docdir}/%{name}
install -m644 LICENSE.md %{buildroot}%{_licensedir}/%{name}

%files -n fonts-ttf-nerd-iosevka
%doc README.md
%{_datadir}/fonts/TFF/*
%{_datadir}/licenses/*
