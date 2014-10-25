%define rbname rsvg2

Summary:	Ruby binding of librsvg-2.x
Name:		rubygem-%{rbname}
Version:	2.2.0
Release:	1
License:	LGPLv2.1+
Group:		Development/Ruby
Url:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygem-cairo-devel
BuildRequires:	rubygem-glib2-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(ruby)
BuildRequires:	rubygem(cairo)
BuildRequires:	rubygem(glib2)

%description
Ruby binding of librsvg-2.x.

%files
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

