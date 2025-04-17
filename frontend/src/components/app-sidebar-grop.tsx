import { Fragment } from 'react'
import {
	SidebarGroup,
	SidebarGroupContent,
	SidebarGroupLabel,
	SidebarMenu,
	SidebarMenuButton,
	SidebarMenuItem
} from '@/components/ui/sidebar'
import { Archive, Book, Megaphone, Search, Settings, UsersRound } from 'lucide-react'

const appMenuItems = [
	{
		group: 'General',
		items: [
			{
				title: 'Search',
				url: '/search',
				icon: Search
			},
			{
				title: 'Announcement',
				url: '/announcement',
				icon: Megaphone
			},
			{
				title: 'Archive',
				url: '/archive',
				icon: Archive
			},
			{
				title: 'Report',
				url: '/report',
				icon: Book
			}
		]
	},
	{
		group: 'Admin',
		items: [
			{
				title: 'Users',
				url: '/users',
				icon: UsersRound
			},
			{
				title: 'Settings',
				url: '/settings',
				icon: Settings
			}
		]
	}
]

export function AppSidebarGroup() {
	return (
		<Fragment>
			{appMenuItems.map(group => (
				<SidebarGroup key={group?.group}>
					<SidebarGroupLabel>{group?.group}</SidebarGroupLabel>
					<SidebarGroupContent>
						<SidebarMenu>
							{group?.items?.map(item => (
								<SidebarMenuItem key={item?.title}>
									<SidebarMenuButton asChild>
										<a
											href={item?.url ?? ''}
											className="flex items-center gap-2"
										>
											<item.icon className="w-4 h-4" />
											<span>{item?.title ?? ''}</span>
										</a>
									</SidebarMenuButton>
								</SidebarMenuItem>
							))}
						</SidebarMenu>
					</SidebarGroupContent>
				</SidebarGroup>
			))}
		</Fragment>
	)
}
