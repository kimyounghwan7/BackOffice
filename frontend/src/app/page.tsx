'use client'
import { Button } from '@/components/ui/button'
import {
	Card,
	CardContent,
	CardDescription,
	CardFooter,
	CardHeader,
	CardTitle
} from '@/components/ui/card'
import { Input } from '@/components/ui/input'
import { Label } from '@radix-ui/react-label'
import { useRouter } from 'next/navigation'
import { Fragment } from 'react'

export default function Home() {
	const router = useRouter()

	const loginSubmit = () => {
		router.push('/dashboard')
	}

	return (
		<Fragment>
			<div className="flex items-center justify-center min-h-screen bg-gray-100">
				<Card className="w-full max-w-sm">
					<CardHeader>
						<CardTitle className="text-center">로그인</CardTitle>
						<CardDescription className="text-center">
							계정 정보를 입력하세요.
						</CardDescription>
					</CardHeader>
					<CardContent>
						<form>
							<div className="grid gap-4">
								<div>
									<Label htmlFor="email">아이디</Label>
									<Input id="email" type="email" placeholder="you@example.com" />
								</div>
								<div>
									<Label htmlFor="password">비밀번호</Label>
									<Input id="password" type="password" />
								</div>
							</div>
						</form>
					</CardContent>
					<CardFooter>
						<Button className="w-full" onClick={loginSubmit}>
							로그인
						</Button>
					</CardFooter>
				</Card>
			</div>
		</Fragment>
	)
}
