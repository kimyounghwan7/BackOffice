'use client'
import { Fragment } from 'react'
import { DataTable } from '@/components/data-table'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs'

export default function TotalSearch() {
	return (
		<Fragment>
			<div className="flex w-full gap-2 px-4">
				<Tabs defaultValue="search" className="w-[400px]">
					<TabsList className="grid w-full grid-cols-2">
						<TabsTrigger value="search">일반 검색</TabsTrigger>
						<TabsTrigger value="ai-search">AI 검색</TabsTrigger>
					</TabsList>
				</Tabs>
			</div>
			<div className="flex w-full gap-2 px-4">
				<Input className="flex-auto" type="text" />
				<Button className="flex-auto" variant={'default'}>
					검색
				</Button>
			</div>
			<div className="flex w-full flex-1 flex-col gap-2 px-4">
				<DataTable columns={[]} data={[]} />
			</div>
		</Fragment>
	)
}
