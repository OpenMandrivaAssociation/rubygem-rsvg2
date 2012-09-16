# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	rsvg2

Summary:	Ruby binding of librsvg-2.x.
Name:		rubygem-%{rbname}

Version:	1.1.5
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  rubygem(glib2)
BuildRequires:  rubygem-glib2-devel
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(librsvg-2.0)

%description
Ruby binding of librsvg-2.x.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

#%package    devel                                                                                                                                                                                              
#Summary:    Development files for %{name}
#Group:      Development/Ruby

#%description	devel
#Development files for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
#%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
#%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
#%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/pkg-config
#%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/pkg-config/*.rb
#%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/test
#%{ruby_gemdir}/gems/%{rbname}-%{version}/test/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

#%files devel
#%{ruby_sitearchdir}/*.h

%changelog

