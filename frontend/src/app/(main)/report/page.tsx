'use client'
import { Fragment } from 'react'
import { DataTable } from '@/components/data-table'
import { Button } from '@/components/ui/button'
import {
	Select,
	SelectContent,
	SelectItem,
	SelectTrigger,
	SelectValue
} from '@/components/ui/select'
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs'

export default function ArchiveList() {
	return (
		<Fragment>
			<div className="flex flex-row gap-2 px-4 justify-between">
				<div className="basis-lg flex flex-row gap-2">
					<Select>
						<SelectTrigger className="flex-auto w-[180px]">
							<SelectValue placeholder="전체" />
						</SelectTrigger>
						<SelectContent>
							<SelectItem value="light">Light</SelectItem>
							<SelectItem value="dark">Dark</SelectItem>
							<SelectItem value="system">System</SelectItem>
						</SelectContent>
					</Select>
					<Tabs defaultValue="search" className="flex-auto w-[400px]">
						<TabsList className="grid w-full grid-cols-2">
							<TabsTrigger value="search">보고서</TabsTrigger>
							<TabsTrigger value="ai-search">임시 보관함</TabsTrigger>
						</TabsList>
					</Tabs>
				</div>
				<div className="basis-sm w-full grid justify-items-end">
					<Button className="max-w-[8rem] flex-1" variant={'default'}>
						작성하기
					</Button>
				</div>
			</div>
			<div className="flex w-full flex-1 flex-col gap-2 px-4">
				<DataTable columns={[]} data={[]} />
			</div>
		</Fragment>
	)
}
