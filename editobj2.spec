%define	oname	EditObj2

Name: 	 	editobj2
Summary: 	Tkinter dialog box for editing any Python object
Version: 	0.4
Release: 	%mkrel 1
Source:		EditObj2-%{version}.tar.gz
URL:		http://home.gna.org/oomadness/en/editobj/
License:	GPLv2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%py_requires -d
Requires:	tkinter
Obsoletes:	editobj
BuildArch:	noarch

%description
EditObj2 can create and display a Tkinter dialog box for editing any Python
object (similarly to what Java call a Bean editor, but for Python object).
EditObj2 is a useful tool for writing (text or non-text) editors of all
kinds, including GUI editor, 3D editor,... It also includes a Python console.

EditObj2 supports also lists, dictionaries and hierarchies (nested lists)
edition. EditObj2 includes also a tree widget for Tkinter, an event framework
and a mutiple undo/redo system.

%prep
%setup -q -n %{oname}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS LICENSE README 
%{python_sitelib}/%{name}
%{python_sitelib}/*.egg-info


%changelog
* Sat Oct 08 2011 Andrey Bondrov <abondrov@mandriva.org> 0.4-1mdv2012.0
+ Revision: 703572
- New version: 0.4

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.2.1-2mdv2011.0
+ Revision: 590801
- rebuild for py2.7

* Sun Apr 18 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.2.1-1mdv2010.1
+ Revision: 536464
- import editobj2


